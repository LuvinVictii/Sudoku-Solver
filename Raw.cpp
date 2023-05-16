#include<bits/stdc++.h>
using namespace std;

int board[9][9];						//board sudokunya
stack<pair<int, int> > ans_loc;			//lokasi kotak yg udah keisi (terurut dari atas kiri ke kanan, ke bawah)
deque<pair<int, int> > blank_loc;		//lokasi kotak yg masih kosong (terurut dari atas kiri ke kanan, ke bawah)

//print boardnya
void print(){
	cout << endl;
	for(int i = 0; i < 9; i++){
		for(int j = 0; j < 9; j++){
			cout << board[i][j];
		}
		cout << endl;
	}
}

//backtrack filling
bool fill(){
	int ii, jj; 		//lokasi kotak yg pengen diisi
	pair<int, int> loc; //pair buat nyimpen front blank_loc
	bool cek[10]; 		//buat cek di kotak kosong itu bisa diisi apa aja
	
	//kalo udah gak ada kotak kosong, return true dan beruntun sampe ke main
	if(blank_loc.empty()) return true;
	
	memset(cek, true, sizeof(cek));	//awalnya semua nomor available di kotak kosong tsb
	
	//loc nyimpen frontnya blank_loc, trus disimpen juga ke ii sama jj
	loc = blank_loc.front();
	ii = loc.first;
	jj = loc.second;
	
	//cek secara vertikal
	for(int i = 0; i < 9; i++){
		if(i == ii) continue;
		cek[board[i][jj]] = false;
	}
	
	//cek secara horizontal
	for(int j = 0; j < 9; j++){
		if(j == jj) continue;
		cek[board[ii][j]] = false;
	}
	
	//cek kotak-kotak se kotak 3x3
	for(int i = ((ii/3)*3); i < ((ii/3)*3) + 3; i++){
		for(int j = ((jj/3)*3); j < ((jj/3)*3) + 3; j++){
			if(i == ii && j == jj) continue;
			cek[board[i][j]] = false;
		}
	}
	
	//ngecek jawaban satu-satu
	for (int i = 1; i <= 9; i++){
		if(cek[i]){ //kalo kotak kosong bisa diisi i
			board[ii][jj] = i;		//ngisi kotaknya
			ans_loc.push(loc);		//keep track lokasi kotak yang barusan diisi
			blank_loc.pop_front();	//kotak kosong udah dianggep ga kosong lagi
			
			//kalo semua kotak terisi dengan benar.
			//klo ternyata salah, dia bakal ganti angka selanjutnya yg available
			if(fill()){
				return true;
			}
		}
	}
	
	//kalo gak ada yang bener, berarti salah di sebelum-sebelumnya. dia bakal ngebacktrack
	if(!ans_loc.empty()){
		blank_loc.push_front(ans_loc.top());	//kotaknya dianggep kosong lagi, dan dicatet lokasinya
		ans_loc.pop();
	}
	board[ii][jj] = 0;						//kotaknya dibalikin jadi 0
	return false;
}

int main(){
	int num;				//hasil translate char ke int
	char temp;				//inputan char
	pair<int, int> loc;		//temporary variable. buat masukin ke deque dalam bentuk pair
	
	//perintah dan aturan input
	cout << "Input unsolved sudoku\n";
	cout << "Input without spaces\n";
	cout << "You can seperate each rows with new line (enter)\n";
	cout << "You can replace blank boxes with any character except 1-9\n\n";
	
	//input
	for(int i = 0; i < 9; i++){
		for (int j = 0; j < 9; j++){
			cin >> temp;
			
			//translate char ke int, masukin ke board, dan data kotak yang kosong
			if(temp < '1' || temp > '9'){
				board[i][j] = 0;
				loc.first = i;
				loc.second = j;
				blank_loc.push_back(loc);
			}
			else board[i][j] = temp - '0';
		}
	}
	
	//kalo valid
	if(fill()){
		print();
	}
	
	//kalo gak valid
	else cout << "\nSudoku is invalid!\n";
	
	return 0;
}
