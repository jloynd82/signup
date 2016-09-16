#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>signup</title>
</head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        error1 = self.request.get("error1")
        error2 = self.request.get("error2")
        error3 = self.request.get("error3")
        error4 = self.request.get("error4")
        username = self.request.get("username")
        email = self.request.get("email")
        text_form="""
        <h2>Signup</h2>
        <form action="/welcome">
            <table>
                <tbody>
                    <tr>
                        <td class="label">Username</td>
                        <td>
                            <input type="text" name="username" value={4}>
                        </td>
                        <td class="error">{0}</td>
                    </tr>
                    <tr>
                        <td class="label">Password</td>
                        <td>
                            <input type="password" name="password" value>
                        </td>
                        <td class="error">{1}</td>
                    </tr>
                    <tr>
                        <td class="label">Verify Password</td>
                        <td>
                            <input type="password" name="verify" value>
                        </td>
                        <td class="error">{2}</td>
                    </tr>
                    <tr>
                        <td class="label">Email (optional)</td>
                        <td>
                            <input type="text" name="email" value={5}>
                        </td>
                        <td class="error">{3}</td>
                    </tr>
                </tbody>
            </table>
            <input type="submit">
        </form>

        """.format(error1, error2, error3, error4, username, email)
        self.response.write(page_header+text_form+page_footer)
    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")
        errors = ["","","",""]
        preserve = ""
        if user == "":
            errors[0] = "You have to enter a username!"
        if password == "":
            errors[1] = "You have to enter a password!"
        if not password == verify:
            errors[2] = "The passwords do not match!"
        if not "@" in email and not "." in email and email != "":
            errors[3] = "Please enter a valid email!"
        error = "?"
        first = True
        for i in range(len(errors)):
            if errors[i] != "":
                if first == False:
                    error += "&error{0}={1}".format(i + 1,errors[i])
                else:
                    error += "error{0}={1}".format(i + 1,errors[i])
                    first = False
        if not username == "" and not email =="":
            preserve += "&username={0}&email={1}".format(username, email)
        elif not username == "":
            preserve += "&username={0}".format(username)
        elif not email == "":
            preserve += "&email={0}".format(email)

        if error != "?":
            self.redirect("/{0}{1}".format(error, preserve))



class Welcome(webapp2.RequestHandler):
    def get (self):
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")
        errors = ["","","",""]
        preserve = ""
        if username == "":
            errors[0] = "You have to enter a username!"
        if password == "":
            errors[1] = "You have to enter a password!"
        if not password == verify:
            errors[2] = "The passwords do not match!"
        if not "@" in email and not "." in email and email != "":
            errors[3] = "Please enter a valid email!"
        error = "?"
        first = True
        for i in range(len(errors)):
            if errors[i] != "":
                if first == False:
                    error += "&error{0}={1}".format(i + 1,errors[i])
                else:
                    error += "error{0}={1}".format(i + 1,errors[i])
                    first = False
        if not username == "" and not email =="":
            preserve += "&username={0}&email={1}".format(username, email)
        elif not username == "":
            preserve += "&username={0}".format(username)
        elif not email == "":
            preserve += "&email={0}".format(email)

        if error != "?":
            self.redirect("/{0}{1}".format(error, preserve))
        self.response.write("Welcome "+username+"!")







app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
