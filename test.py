import xml.etree.ElementTree as ET
import importlib.util
import sys

def test():
    sys.path.append('students/Stefan Niculae/add')

    assignment_file = sys.argv[1]

    tree = ET.parse('assignments/' + assignment_file)
    root = tree.getroot()
    assignment = root[0]
    assignment_name = assignment.get("name")
    language = assignment.find("language").text
    title = assignment.find("title").text
    text = assignment.find("text").text
    parameters = assignment.find("parameters").text.split(" ")
    tests = assignment.find("tests")
    print(5 * '-' + title + 5 * '-')
    print(text)
    target = importlib.util.spec_from_file_location("add", "students/Bianca Savu/" + assignment_name + "/" + assignment_name + ".py")
    foo = importlib.util.module_from_spec(target)
    target.loader.exec_module(foo)
    function = foo.add
    
    for t in tests.findall("test"):
        test_name = t.get("name")
        input = t.find("input").text
        output = t.find("output").text
        points = t.find("points").text
        input = input.split(" ")
        p_input = []
        for i in input:
            p_input.append(float(i))
        print ()
        print(p_input)
        print(function(*p_input))

if __name__ == '__main__':
    test()
