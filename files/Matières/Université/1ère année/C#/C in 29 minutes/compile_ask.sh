echo "Enter the name of the file to compile:"
name=read
echo "Enter the name of the destination file:"
destname=read
gcc `destname` -o `name`
echo "$destanme compiled"
echo "Running $destname.out"
"$destanme.out"
echo `name`