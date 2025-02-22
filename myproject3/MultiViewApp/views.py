from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input1(request):
    str1='''
    <html>
        <body bgcolor="yellow" text="red">
            <center>
                <h1><b><u>EMPLOYEE DETAILS</b></u></h1>
                <table border=5>
                    <tr>
                        <th>EMPID</th>
                        <th>EMPNAME</th>
                        <th>SALARY</th>
                        <th>DESIGNATION</th>
                    </tr>
                    <tr>
                        <td>101</td>
                        <td>JOHN</td>
                        <td>1000000</td>
                        <td>Manager</td>
                    </tr>
                    <tr>
                        <td>102</td>
                        <td>TIM</td>
                        <td>1000000</td>
                        <td>Clear</td>
                    </tr>
                    <tr>
                        <td>103</td>
                        <td>SMITH</td>
                        <td>1000000</td>
                        <td>Professor</td>
                    </tr>
                </table>
            </center>
        </body>
    </html>
    '''
    return HttpResponse(str1)

def input2(request):
    str2='''
    <html>
        <body bgcolor="red" text="yellow">
            <center>
                <h1><b><u>CUSTOMER DETAILS</b></u></h1>
                <table border=5>
                    <tr>
                        <th>CUSTID</th>
                        <th>CUSTNAME</th>
                        <th>BALANCE</th>
                        <th>CITY</th>
                    </tr>
                    <tr>
                        <td>101</td>
                        <td>JOHN</td>
                        <td>1000000</td>
                        <td>Almere</td>
                    </tr>
                    <tr>
                        <td>102</td>
                        <td>TIM</td>
                        <td>1000000</td>
                        <td>Amsterdam</td>
                    </tr>
                    <tr>
                        <td>103</td>
                        <td>SMITH</td>
                        <td>1000000</td>
                        <td>Den Haag</td>
                    </tr>
                </table>
            </center>
        </body>
    </html>
    '''
    return HttpResponse(str2)

def input3(request):
    str3='''
    <html>
        <body bgcolor="red" text="yellow">
            <center>
                <h1><b><u>STUDENT DETAILS</b></u></h1>
                <table border=5>
                    <tr>
                        <th>STDID</th>
                        <th>STDNAME</th>
                        <th>MARKS</th>
                        <th>COLLEGE</th>
                    </tr>
                    <tr>
                        <td>101</td>
                        <td>JOHN</td>
                        <td>65</td>
                        <td>Utrecht University</td>
                    </tr>
                    <tr>
                        <td>102</td>
                        <td>TIM</td>
                        <td>35</td>
                        <td>Virj University</td>
                    </tr>
                    <tr>
                        <td>103</td>
                        <td>SMITH</td>
                        <td>90</td>
                        <td>Amsterdam University</td>
                    </tr>
                </table>
            </center>
        </body>
    </html>
    '''
    return HttpResponse(str3)
