# ShiftOrganizer
a software for shift assignment.

How to use?

In order to Add a worker to the Database -

![image](https://github.com/noamst/ShiftOrganizer/assets/19705801/f26338b8-7748-45ca-931f-f5e006f2857c)


![image](https://github.com/noamst/ShiftOrganizer/assets/19705801/c7f7e3dd-d1c5-403f-abe7-40ba5c80c8ad)


In order to Add a constraint (worker X cannot work on shift Y) -

![image](https://github.com/noamst/ShiftOrganizer/assets/19705801/ebda871b-4041-4f88-bcfe-5c9f504bb13d)

![image](https://github.com/noamst/ShiftOrganizer/assets/19705801/e9c37672-bc3c-42ae-9990-3599da804420)

(You can verify if an ID exists , the second blank is to add a new shift in which the worker cannot work)


![image](https://github.com/noamst/ShiftOrganizer/assets/19705801/ca1332c6-3442-459e-8bb5-4d2a1d53e8f5)


Last Button is to run the algorithm (I came up with a reduction to max-flow algorithm in order to solve this problem)
and calculate the assignments


You can also check current constraints if you specify the ID of the worker you are interested in -

![image](https://github.com/noamst/ShiftOrganizer/assets/19705801/7575dba2-cf4b-47f3-89ff-1d524abdbdc4)

Ultimately after calculation the output will be a txt file that will include assignment to the shifts



