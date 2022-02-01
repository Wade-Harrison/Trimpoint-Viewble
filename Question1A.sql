SELECT name_table.StudentID, name_table.Name

FROM name_table

left JOIN marks_table

ON name_table.StudentID = marks_table.StudentID

WHERE Total_marks > (SELECT Total_marks FROM marks_table

where studentID = 'V002')

;