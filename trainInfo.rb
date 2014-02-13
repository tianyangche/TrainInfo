#!/usr/bin/ruby
require 'csv'
#result = CSV.read("test1.csv")
#csv_text = File.read("test1.csv")
#csv = CSV.parse(csv_text, :headers=> false)
#result = csv[1..-1]
#puts result[1]

arr = []
CSV.foreach("test1.csv") do |row|
	arr << row
end
arr = arr[1..-1]
result = arr.sort {|a,b| a[2] <=> b[2]}
puts "Train Line\tRoute\t\tRun Number\tOperator ID"
for i in 0..result.count-1
puts result[i][0]+"\t\t"+result[i][1]+"\t"+result[i][2]+"\t\t"+result[i][3]
end
