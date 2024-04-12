# a_lazy_observation
observe the correlation between c++ function memory addresses on your system

currently only linux is supported bc this was an anti-boredom project in a friday afternoon, so...

(maybe I'll expand it with cmake or sth just for to excercise a bit, but that's a big maybe!)

#anyways

simply do:
<code>
chmod +x ./run.sh 
./run.sh
</code>

if u wanna know what run does, read it!

if u wanna change the number of stupid functions generated change the generate_arbitrary_functions.py 's 
source where it says 
FUNCS_NUM=5

the same goes for FUNCS_TYPES and FUNCS_RETURN

note to change the two accordingly:

if you have "void" for FUNCS_TYPES, change FUNCS_RETURN to "return" or ""

#depenedencies

<code>
python3 
gcc (g++ with -std=c++17 in this case)
linux!
vim (bc other text editors are for lifetime drunkard rotten-milk drinking alcoholics!)
</code>

peace!
