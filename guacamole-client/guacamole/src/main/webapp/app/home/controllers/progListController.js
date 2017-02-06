angular.module('home').controller('progListController', ['$scope', function($scope) {
  $scope.picturePath = "images/";
  $scope.progListItems = [ 
    { 
      id: "distrib.py",
      name: "Python Distribute",
      details: "Description: clicking on the canvas adds a turtle; all the turtles will distribute themselves evenly across the canvas.",
      image: $scope.picturePath + "distrib_py.png" //"http://i63.tinypic.com/23jhiqr.png"
    }, 
    { 
      id: "tkintertest2.py",
      name: "Python Calculator",
      details: "Description: A simple calculator program.",
      image: $scope.picturePath + "python_calculator.png" //"http://i63.tinypic.com/eja1qw.png"
    },
    {
      id: "gui.py",
      name: "Solitaire",
      details: "A Solitaire-like Card Game"
    },
    {
      id: "main.py",
      name: "Mario Cart",
      details: "Click below to run the program."
    },
    {
      id: "driver.py",
      name: "Snake",
      details: "A clone of the classic Snake game.",
      image: $scope.picturePath + "snake.png" //"http://i65.tinypic.com/261ewci.png"
    },
    {
      id: "driver.py",
      name: "Othello (Kinda)",
      details: "Othello game (mostly broken).",
      image: $scope.picturePath + "othello.png" //"http://i64.tinypic.com/2eao32g.png"
    },
    {
      id: "driver.py",
      name: "Super Tic Tac Toe",
      details: "Not your grandma's tic tac toe -IGN"
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
    },
      ];
}]);
