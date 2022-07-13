
def findChar_Diff(inputData1='' ,inputData2=''):
    print(f'Input Data 1 {inputData1}')
    print(f'Input Data 2 {inputData2}')
    if inputData1 is None or inputData2 is None:
        print("Number of Same Characters: 0")
        return

    response =''
    size = len(inputData1)
    for i in range(size):
        if str(inputData1[i]) not in inputData2:
            response += inputData1[i]

    if response is None or response == '':
        response += '<null>'

    return response

if __name__ == '__main__':

    inputData1 = 'abc'
    inputData2 = 'bc'
    response =  findChar_Diff(inputData1, inputData2)
    print(f'Difference between input1 and input2 {response}')
    response =  findChar_Diff(inputData2, inputData1)
    print(f'Difference between input2 and input1 {response}')

    inputData1 = 'bc'
    inputData2 = 'bangalore'
    response =  findChar_Diff(inputData1, inputData2)
    print(f'Difference between input1 and input2 {response}')
    response =  findChar_Diff(inputData2, inputData1)
    print(f'Difference between input2 and input1 {response}')

