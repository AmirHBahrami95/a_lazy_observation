#include <iostream>

static long addresses[5];
static int ap=0;
static long rshit[5]; // who cares!
static int rp=0; 

void adshit(long addr);
void subshit(long addr,long addr1);
void printShit(long shit[],char hex);
void printShit(long shit[]);

int shit0(){std::cout<<"shit0"<<std::endl;return 0;}
int shit1(){std::cout<<"shit1"<<std::endl;return 0;}
int shit2(){std::cout<<"shit2"<<std::endl;return 0;}
int shit3(){std::cout<<"shit3"<<std::endl;return 0;}
int shit4(){std::cout<<"shit4"<<std::endl;return 0;}
/*-------------------------------------------------------------------*/

int main(){


	adshit((long)shit0);
	subshit((long)shit0,(long)shit1);
	adshit((long)shit1);
	subshit((long)shit1,(long)shit2);
	adshit((long)shit2);
	subshit((long)shit2,(long)shit3);
	adshit((long)shit3);
	subshit((long)shit3,(long)shit4);

	printShit(addresses,'h');
	std::cout<<"--------------------------------------"<<std::endl;
	printShit(rshit,'d');
	return 0;
}

void printShit(long shit[],char hex){
	if(hex=='h')
		std::cout<<std::hex;
	else
		std::cout<<std::dec;
	for(int i=0;shit[i]!=-1 && i<5;i++)
		std::cout<<shit[i]<<std::endl;
}

void printShit(long shit[]){
	printShit(shit,'d');
}

void adshit(long addr){
	for(int i=0;i<ap && addresses[i]==addr;i++);
	addresses[ap]=addr;
	ap++;
	addresses[ap]=-1; // for uniform printing later
}
void subshit(long addr,long addr1){
	rshit[rp]=addr1-addr;
	rp++;
	rshit[rp]=-1;
}

