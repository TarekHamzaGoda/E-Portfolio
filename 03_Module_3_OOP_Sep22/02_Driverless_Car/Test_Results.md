
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
