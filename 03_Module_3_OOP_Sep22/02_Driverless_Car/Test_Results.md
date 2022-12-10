<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>Test Results</h1>
<p><strong>Assignment Part II</strong></p>
<hr />
<h2>Basic Test Instructions</h2>
<hr />
<ol>
<li>Run the code</li>
<li>Insert username. &ldquo;defaultd&rdquo; <em>Default Driver</em></li>
<li>Select any option by inputing the desired number</li>
<li>Once testing is concluded, go to car log in</li>
<li>Compare car log with expected test results</li>
</ol>
<hr />
<h2>Car Controls and state.</h2>
<hr />
<p>This test aims to examine the car controls and state <em>(starting, speed, stopping)</em></p>
<h4>Sequence</h4>
<hr />
<p><strong>car state:</strong>
<br  />1.car info
<br  />2.car status</p>
<p><strong>car drive:</strong>
<br  />2.car drive
<br  />1.Start the car
<br  />2.accelerate
<br  />3.Change lane</p>
<h4>Expected test result</h4>
<hr />
<p><strong>car state:</strong>
<br  />car type: Car
<br  />speed: 0
<br  />Direction: N
<br  />Lane: 1
<br  /><strong>car drive:</strong>
<br  />Car started, car is moving at 30 km/h
<br  />Car now is moving at 50 km/h.
<br  />Lane changed to 2</p>
<hr />
<h2>Car Log Feature</h2>
<hr />
<p>This test aims to examine the control unit event log</p>
<h4>Sequence</h4>
<hr />
<p>7.Main menu
<br  />1.Car info
<br  />2.View car Log
<br  />6.Main menu
<br  />3.Car settings
<br  />1.Insert obstacle</p>
<h4>Expected test result</h4>
<hr />
<p>Record                                                                               Time Stamp
<br  />Car lane changed to  2.                                                              06/12/2022 01:37:23
<br  />The car decelerated to 30 km/h.                                                      06/12/2022 01:36:38
<br  />Car is accelerated to 50 km/h.                                                       06/12/2022 01:36:23
<br  />Car is on and moving at speed of 30 km/h                                             06/12/2022 01:36:02
<br  />Driver 'defaultd' is now authorized to use the system.                               06/12/2022 01:35:11</p>
<p>Current lane is 2, object lane is 1. No action needed</p>
<hr />
<h2>Objects, Traffic signs, Vehicle insertion, and detection.</h2>
<hr />
<p>This test aims to examine the car control function <em>(starting, speed, stopping)</em></p>
<h4>Sequence</h4>
<hr />
<p>3.Car settings
<br  />3.Insert Car
<br  />1.Sedan
<br  />(120)speed
<br  />(n)Direction
<br  />(1)Lane
<br  />6.Main menu
<br  />1.Car info
<br  />2.View car Log</p>
<h4>Expected result</h4>
<hr />
<p>Car on different lane, no action needed
<br  />Record                                                                               Time Stamp
<br  />Car detected at Lane 1 and Direction: N. no action needed                            06/12/2022 01:44:06
<br  />Driver 'defaultd' is now authorized to use the system.                               06/12/2022 01:43:48</p>
</div>