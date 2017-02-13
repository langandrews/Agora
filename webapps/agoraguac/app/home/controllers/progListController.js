angular.module('home').controller('progListController', ['$scope', function($scope) {
  $scope.runButton = "images/grey_run_button.png";
  $scope.picturePath = "images/";
  $scope.progListItems = [ 
    { 
      id: "distrib.py",
      name: "Python Distribute",
      details: "Description: clicking on the canvas adds a turtle; all the turtles will distribute themselves evenly across the canvas.",
      image: $scope.picturePath + "distrib_py.png",
			instructions: "Simply click on any blank area of the background to place a turtle there.  The turtles will then automatically try to  distribute themselves in the space.",
      author: "Victor Norman",
      date: "Before Fall 2017"
    }, 
    { 
      id: "tkintertest2.py",
      name: "Python Calculator",
      details: "Description: A simple calculator program.",
      image: $scope.picturePath + "python_calculator.png",
			instructions: "Type in values and hit + or - to calculate.  The result is displayed in the top right corner of the window.  Hit reset to begin a new calculation.",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "gui.py",
      name: "Solitaire",
      details: "A Solitaire-like Card Game",
      image: $scope.picturePath + "solitaire.png",
			instructions: "This is a form of solitaire that has a really long set of instructions.",
      author: "Prof Norman",
      date: "Feb 6, 2017"
    },
    {
      id: "main.py",
      name: "Mario Kart",
      details: "Click below to run the program.",
      image: $scope.picturePath + "mariokart.png",
			instructions: "Use wasd or ijkl to race your opponent around the racetrack.  Try not to stray off the track, or else your speed will be dramatically reduced!",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "driver.py",
      name: "Snake",
      details: "A clone of the classic Snake game.",
      image: $scope.picturePath + "snake.png",
			instructions: "Use the arrow keys to control your snake's movement.  Collect the red things to get longer.  Going off the edge on one side results in showing up on the other.",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "driver.py",
      name: "Othello (Kinda)",
      details: "Othello game (mostly broken).",
      image: $scope.picturePath + "othello.png",
			instructions: "This game doesn't actually work, so don't play it.",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "driver.py",
      name: "Super Tic Tac Toe",
      details: "Not your grandma's tic tac toe -IGN",
      image: $scope.picturePath + "super_tictactoe.png",
			instructions: "Instructions coming soon.",
      author: "Unknown",
      date: "Before Fall 2017"
    },
    {
      id: "GuiApp1",
      name: "Java Gui",
      details: "Java test...",
			instructions: "Really nothing to do here.  Just look and enjoy! :)",
      author: "Joel Stehouwer",
      date: "Fall 2017"
    },
    {
      id: "HelloWorld",
      name: "Java Console",
      details: "Java test, check logs/java_try.log...",
			instructions: "Really nothing to do here.  Just look and enjoy! :)",
      author: "Joel Stehouwer",
      date: "Fall 2017"
    },
    {
      id: "main",
      name: "C++ Console",
      details: "C++ program",
			instructions: "Really nothing to do here.  Just look and enjoy! :)",
      author: "Joel Stehouwer",
      date: "Fall 2017"
    },
    {
      id: "hello.exe",
      name: "C# Console",
      details: "C# program",
			instructions: "Really nothing to do here.  Just look and enjoy! :)",
      author: "Andrew Lang",
      date: "Fall 2017"
    },
    {
      id: "CSharpGui.exe",
      name: "C# Gui",
      details: "C# Gui Program",
			instructions: "Really nothing to do here.  Just look and enjoy! :)",
      author: "Andrew Lang",
      date: "Fall 2017"
    },
      ];
}]);
