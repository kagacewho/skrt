input_data = open('input.txt', 'r') 
data = input_data.read()
N = int(data)
sum = 0
if N > 0:
    sum=0
for i in range(0,N+1,1):
    sum+=i
else:
    range(N,1,1)
output_data = open('output.txt', 'w')
output_data.write(str(sum))
input_data.close()
output_data.close()