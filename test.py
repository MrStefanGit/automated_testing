import xml.etree.ElementTree as ET
import importlib.util
import sys
import os

def test():
    sys.path.append('students/Stefan Niculae/add')

    assignment_file = sys.argv[1]

    students_path = "./students"
    students = os.listdir(students_path)

    tree = ET.parse('assignments/' + assignment_file)
    root = tree.getroot()
    assignment = root[0]
    assignment_name = assignment.get("name")
    language = assignment.find("language").text
    title = assignment.find("title").text
    text = assignment.find("text").text
    parameters = assignment.find("parameters").text.split(" ")
    output_type = assignment.find("outputType").text
    input_type = assignment.find("inputType").text
    tests = assignment.find("tests")
    
    print('\n' + 5 * '*' + title.upper() + 5 * '*')
    print(text)
    print(100 * '-')
    grades = {}
    for s in students:
        print('\n' + 5 * '-' + 'Student: ' + s + 5 * '-')
        total_points = 0
        grades[s] = 0
        try:
            target = importlib.util.spec_from_file_location("function", "students/" + s + "/" + assignment_name + "/" + assignment_name + ".py")
            foo = importlib.util.module_from_spec(target)
            target.loader.exec_module(foo)
            function = foo.function
        except:
            print('Student has not submitted this assignment')
            continue
        
    
        for t in tests.findall("test"):
            obtained_points = 0
            test_name = t.get("name")
            input = t.find("input").text
            output = t.find("output").text
            points = t.find("points").text
            
            p_input = []
            if input_type == 'float':
                input = input.split(" ")
                for i in input:
                    p_input.append(float(i))
            elif input_type == 'list':
                input = input.split(" ")
                for i in input:
                    tmp = i[1:len(i)-1]
                    p_input.append(tmp.split(','))
                for l in p_input:
                    for i in range(0, len(l)):
                        l[i] = int(l[i])

            print ()
            print(50 * '-')
            print('Test: ' + test_name)
            print('Input: {}'.format(p_input))
            print('Expected output: ' + output)
            print('Recived output: {}'.format(function(*p_input)))
            total_points += int(points)
            if output_type == 'float':
                if (float(output) == function(*p_input)):
                    obtained_points += int(points)
                    grades[s] += obtained_points
            elif output_type == 'list':
                output = output.split(" ")
                for i in range(0, len(output)):
                    output[i] = int(output[i])
                if (output == list(function(*p_input))):
                    obtained_points += int(points)
                    grades[s] += obtained_points
            
            print('-Obtained {} points out of {} maximum points'.format(obtained_points, points))
            print(50 * '-')
        print(20*'-' + 'Student {} grade: {}/{}'.format(s, grades[s], total_points) + 20*'-' + '\n')

if __name__ == '__main__':
    test()
