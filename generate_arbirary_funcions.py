# this scripts makes functions and useless boilerplate for a .cpp file
# check the "addr_correlation" to see the generated fuck

# the entire reason is that I didn't know how to get c++ functions name
# in a methodic manner (like Java sth-sth API!), so I just came up with
# this banther wank

FUNCS_NUM=5
FUNCS_TYPE="int"
FUNCS_RETURN="return 0"

print ("""#include <iostream>

static long addresses[{}];
static int ap=0;
static long rshit[{}]; // who cares!
static int rp=0; 

void adshit(long addr);
void subshit(long addr,long addr1);
void printShit(long shit[],char hex);
void printShit(long shit[]);
""".format(FUNCS_NUM,FUNCS_NUM))

# make functions
for i in range(0,FUNCS_NUM):
	print("{} shit{}(){}std::cout<<\"shit{}\"<<std::endl;{};{}".format(FUNCS_TYPE,i,'{',i,FUNCS_RETURN,'}'))
print("""/*-------------------------------------------------------------------*/

int main(){

""")

for i in range(0,FUNCS_NUM-1):
	print("\tadshit((long)shit{});".format(i))
	print("\tsubshit((long)shit{},(long)shit{});".format(i,i+1))

print("""
	printShit(addresses,'h');
	std::cout<<"--------------------------------------"<<std::endl;
	printShit(rshit,'d');
	return 0;
}

void printShit(long shit[],char hex){""")

print("""\tif(hex=='h')
\t\tstd::cout<<std::hex;
\telse
\t\tstd::cout<<std::dec;
\tfor(int i=0;shit[i]!=-1 && i<{};i++)""".format(FUNCS_NUM))

print(
"""\t\tstd::cout<<shit[i]<<std::endl;
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
""")
