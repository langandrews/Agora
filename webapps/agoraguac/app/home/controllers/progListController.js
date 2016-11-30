angular.module('home').controller('progListController', ['$scope', function($scope) {
  $scope.progListItems = [ 
    { 
      id: "distrib.py",
      name: "Python Distribute",
      details: "Description: clicking on the canvas adds a turtle; all the turtles will distribute themselves evenly across the canvas."
    }, 
    { 
      id: "tkintertest2.py",
      name: "Python Calculator",
      details: "Description: A simple calculator program."
    },
    {
      id: "main.py",
      name: "Mario Cart",
      details: "Click below to run the program."
    },
    {
      id: "GuiApp1",
      name: "Java Gui",
      details: "Java test..."
    },
    {
      id: "HelloWorld",
      name: "Java Console",
      details: "Java test, check logs/java_try.log..."
    },
    {
      id: "main",
      name: "C++ Console",
      details: "C++ program"
    },
    {
      id: "hello.exe",
      name: "C# Console",
      details: "C# program"
    },
    {
      id: "CSharpGui.exe",
      name: "C# Gui",
      details: "C# Gui Program"
    }
  ];
}]);
