<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>Autonomous Car System Implementation</h1>
<p><strong>Assignment Part II</strong></p>
<hr />
<h2>System Features</h2>
<p>The autonomous car system aims to provide a self-driving experience with the following features:</p>
<ol>
<li>Car Control system <em>(Interacting with detected objects)</em></li>
<li>Car System log <em>(to check car’s state, detected objects and drivers list)</em></li>
</ol>
<p>To simulate the system, the car will be able to move in <strong>opposite</strong> directions and switch between <strong>2</strong> lanes.
<br  />This will be controlled by a series of input options provided to the driver or the user.</p>
<h2>Main system development</h2>
<h4>Imported Modules</h4>
<hr />
<p>There are 3 imported modules to support the system design.</p>
<ol>
<li><strong>ABC(Abstract Classes and Abstract methods) from abc module</strong>: This provides a base class for future implementation.</li>
<li><strong>EXIT from sys</strong>: In order to terminate the car system, the exit() function is added as a user interface command.</li>
<li><strong>Datetime</strong>: The date-time module assist in adding time stamps to the log database.<hr />
<h4>Syntax</h4>
<hr />
<strong>The structure of the syntax consists of 3 code blocks:</strong></li>
</ol>
<p><strong>Section 1</strong>: Abstract Classes and method decorators:</p>
<p>Although the abstract classes that are created are not implemented, it is considered good practice to provide a
<br  />base structure for the system components. As such, the abstract methods will raise <strong>“NotimplementationError”</strong>.
<br  />For each system component, a base class was created as a blueprint. Therefore, the structure of the classes are divided
<br  />into sections that includes <em>(Control Unit and Divers Data), (Car Data and V2V Communication), (Senor and obstacle Detection), (Traffic Signs database).</em></p>
<p><strong>Section 2</strong>: Supper Classes, Classes, Subclasses, Temporary and permanent objects:</p>
<p>Class methods will override the abstract methods to insure the sequence of the interface (Artemis 2021). The created classes represent
<br  />system features such as the control unit, sensor detection, TSRS, as well as a database to store, system information
<br  />car log, sign types and detected objects. permanent objects such as the default driver, senors, and signs database
<br  />are created to initialize the system while temporary objects are created based on the user's/driver input (Sutter 2022).
<br  />This is because a Temporary object stores the data generated by the user’s input and is sent to the correspondent system component.</p>
<p><strong>Section 3</strong>: User Interface Functions and User Instructions:</p>
<p><strong>The user interface consists of a sequence of function in order to be able to simulate the car.</strong></p>
<ol>
<li><strong>Step 1: Driver login:</strong> Considered as the <em>landing page</em> once running the code, this will be the driver’s gateway to
<br  />input his username for authentication.</li>
<li><strong>Step 2: The interface menu</strong> after logging in, the driver is enabled to explore the features present in
<br  />the control unit which includes car controls and car database.</li>
<li><strong>Step 3:information menu</strong> enables the driver to examine the cars state, driver’s list view the system
<br  />log and detected objects. (obstacles,</li>
<li><strong>Car settings:</strong> an interface that allows the user to simulate and modify features in the control unit.
<br  />this interface will allow the driver to insert  obstacles, traffic signs and other smart cars.
<br  />The user will also be able to insert or remove new drivers in the control unit database<hr />
<h4>Data Structure</h4>
<hr />
<strong>Main data structures that are included in the system:</strong>
<br  /><em>Car_log[]</em>: Contains current status, detected objects and surrounding vehicle interactions.
<br  /><em>Obstacles[]</em>: Contains detected obstacles
<br  /><em>driver_db[]</em>: Contains Drivers information
<br  /><em>Obstacle_type{}:</em> Contains obstacle types
<br  /><em>Car_type{}:</em> Contains car types
<br  /><em>Sign_type{}:</em> Contains sign types</li>
</ol>
<hr />
<h4>Testing</h4>
<hr />
<p>Component based <em>validation</em> tests are implemented on system features in 3 test cases.<em>(pytest used for unit testing)</em>:</p>
<ol>
<li><strong>Car Controls and state.</strong>
<br  />Testing car control functions (start, accelerate, stop)</li>
<li><strong>Objects, Traffic signs, Vehicle insertion, and detection</strong>
<br  />Inserting and tested vehicle interaction with obstacles and traffic signs.</li>
<li><strong>Viewing system logs and information.</strong>
<br  />Printing driver's data and detected objects data.</li>
</ol>
<p><em>Test Results Are documented here.</em></p>
<hr />
<h4>References</h4>
<hr />
<p>Artemis , N., 2021. TDS. [Online]
<br  />Available at: https://towardsdatascience.com/how-to-use-abstract-classes-in-python-d4d2ddc02e90
<br  />[Accessed 30 11 2022].</p>
<p>Sutter, H., 2022. Temporary objects. [Online]
<br  />Available at: https://learn.microsoft.com/en-us/cpp/cpp/temporary-objects?view=msvc-170
<br  />[Accessed 30 11 2022].</p>
</div>