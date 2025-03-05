require 'date'

class Student
  attr_accessor :surname, :name, :date_of_birth
  @@students = []

  def initialize(surname, name, date_of_birth)
    @surname = surname
    @name = name
    @date_of_birth = validate_date_of_birth(date_of_birth)
  end

  def validate_date_of_birth(date_of_birth)
    if date_of_birth >= Date.today
      puts "Помилка: Дата народження має бути раніше сьогоднішньої дати."
      return nil
    end
    date_of_birth
  end

  def self.calculate_age(student)
    return nil unless student.date_of_birth

    today = Date.today
    age = today.year - student.date_of_birth.year
    birthday_this_year = Date.new(today.year, student.date_of_birth.month, student.date_of_birth.day)

    age -= 1 if today < birthday_this_year
    age
  end

  def self.add_student(student)
    if student.date_of_birth.nil?
      puts "Студента не додано через некоректну дату народження."
      return
    end

    existing_student = @@students.find do |s| s.name == student.name && s.surname == student.surname && s.date_of_birth == student.date_of_birth end

    if existing_student
      @@students.delete(existing_student)
      puts "Студента #{existing_student.name} #{existing_student.surname} видалено через дублювання."
    end

    @@students << student
    puts "Студент доданий: #{student.name} #{student.surname}"
  end

  def self.remove_student(student)
    if @@students.delete(student)
      puts "Студента #{student.name} #{student.surname} видалено."
    else
      puts "Студента не знайдено в списку."
    end
  end

  def self.get_students_by_age(age)
    students = @@students.select { |s| calculate_age(s) == age }
    if students.empty?
      puts "Студентів з віком #{age} не знайдено."
    else
      students.each { |s| puts "#{s.name} #{s.surname}, Дата народження: #{s.date_of_birth}" }
    end
  end

  def self.get_students_by_name(name)
    list = @@students.select { |s| s.name == name }
    if list.empty?
      puts "Студентів з ім'ям '#{name}' не знайдено."
    else
      list.each { |s| puts "#{s.surname}, #{s.name}, Дата народження: #{s.date_of_birth}" }
    end
  end

  def self.students
    @@students.map { |s| "#{s.name} #{s.surname}, Дата народження: #{s.date_of_birth}" }
  end
end

student1 = Student.new("Surname", "Name", Date.new(2000, 5, 20))
Student.add_student(student1)
student2 = Student.new("Terenov", "Mary", Date.new(1998, 10, 15))
Student.add_student(student2)
student3 = Student.new("Olecsiev", "Mary", Date.new(2001, 12, 1))
Student.add_student(student3)
student4 = Student.new("Melnov", "Alex", Date.new(2025, 1, 10))
Student.add_student(student4)
student5 = Student.new("Olecsiev", "Mary", Date.new(2001, 12, 1))
Student.add_student(student5)

puts "Вік студента #{student1.name} #{student1.surname}: #{Student.calculate_age(student1)}"
puts "Студенти з ім'ям 'Mary':"
Student.get_students_by_name("Mary")
puts "Студенти, які мають 22 роки:"
Student.get_students_by_age(22)
puts "Видалення студента #{student1.name} #{student1.surname}:"
Student.remove_student(student1)
puts "Студенти після видалення:"
puts Student.students