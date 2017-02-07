angular.module('home').controller('progListController', ['$scope', function($scope) {
  $scope.runButton = "images/grey_run_button.png";
  $scope.picturePath = "images/";
  $scope.progListItems = [ 
    { 
      id: "distrib.py",
      name: "Python Distribute",
      details: "Description: clicking on the canvas adds a turtle; all the turtles will distribute themselves evenly across the canvas.",
      image: $scope.picturePath + "distrib_py.png",
      author: "Victor Norman",
      date: "Before Fall 2017"
    }, 
    { 
      id: "tkintertest2.py",
      name: "Python Calculator",
      details: "Description: A simple calculator program.",
      image: $scope.picturePath + "python_calculator.png",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "gui.py",
      name: "Solitaire",
      details: "A Solitaire-like Card Game",
      image: $scope.picturePath + "solitaire.png",
      author: "Prof Norman",
      date: "Feb 6, 2017"
    },
    {
      id: "main.py",
      name: "Mario Kart",
      details: "Click below to run the program.",
      image: $scope.picturePath + "mariokart.png",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "driver.py",
      name: "Snake",
      details: "A clone of the classic Snake game.",
      image: $scope.picturePath + "snake.png",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "driver.py",
      name: "Othello (Kinda)",
      details: "Othello game (mostly broken).",
      image: $scope.picturePath + "othello.png",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "driver.py",
      name: "Super Tic Tac Toe",
      details: "Not your grandma's tic tac toe -IGN",
      image: $scope.picturePath + "super_tictactoe.png",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "GuiApp1",
      name: "Java Gui",
      details: "Java test...",
      author: "Joel Stehouwer",
      date: "Fall 2017"
    },
    {
      id: "HelloWorld",
      name: "Java Console",
      details: "Java test, check logs/java_try.log...",
      author: "Joel Stehouwer",
      date: "Fall 2017"
    },
    {
      id: "main",
      name: "C++ Console",
      details: "C++ program",
      author: "Joel Stehouwer",
      date: "Fall 2017"
    },
    {
      id: "hello.exe",
      name: "C# Console",
      details: "C# program",
      author: "Andrew Lang",
      date: "Fall 2017"
    },
    {
      id: "CSharpGui.exe",
      name: "C# Gui",
      details: "C# Gui Program",
      author: "Andrew Lang",
      date: "Fall 2017"
    },
      ];
}]);
