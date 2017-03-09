angular.module('home').controller('progListController', ['$scope', function($scope) {
  $scope.runButton = "images/grey_run_button.png";
  $scope.picturePath = "images/";
  $scope.progListItems = {
    'cs108': [
        {
          id: "distrib.py",
          name: "Python Distribute",
          details: "Description: clicking on the canvas adds a turtle; all the turtles will distribute themselves evenly across the canvas.",
          image: $scope.picturePath + "distrib_py.png",
          instructions: "Simply click on any blank area of the background to place a turtle there.  The turtles will then automatically try to  distribute themselves in the space.",
          author: "Victor Norman",
          date: "Before Fall 2016"
        },
        {
          id: "tkintertest2.py",
          name: "Python Calculator",
          details: "Description: A simple calculator program.",
          image: $scope.picturePath + "python_calculator.png",
          instructions: "Type in values and hit + or - to calculate.  The result is displayed in the top right corner of the window.  Hit reset to begin a new calculation.",
          author: "Unknown",
          date: "Before Fall 2016"
        },
        {
          id: "gui.py",
          name: "Solitaire",
          details: "A Solitaire-like Card Game",
          image: $scope.picturePath + "solitaire.png",
          instructions: "In this version of Solitaire, the goal is to place all the cards in order from small to largest by suit in as few rounds as possible."+
            "  Thus, to win, each row must have 2 through K of a suit.  Note that Aces are removed to make empty spaces.\n"+
            "Play begins by showing a board of 4 rows and 13 columns, with the Aces removed.  The only moves that can be made are to move certain cards into the 4 empty spaces."+
            "  The only card that can be moved into a space is the card that is the next card high of the same suit as the card immediately to the left of the space."+
            "  E.g., if there is a space that is to the right of the 7 of hearts, the only card that can be moved into that space is the 8 of hearts."+
            "  As there are 4 spaces open at all times, the player has 4 choices of which cards to move.  Cards that eligible to be moved have a yellow rectangle around them.\n"+
            "If a space ends up \"behind\" (i.e., to the right of) a King, then that space is dead -- there is no card that can be moved there."+
            "  Thus, the player should avoid moving cards such that a space ends up to the right of a King.\n"+
            "While it may sound like the player does not have to make many strategic moves, some strategy is useful.  One strategy is to try to recover \"lost spaces\" behind Kings."+
            "  This can be done by moving a King to a new location if it has a space behind it.\n"+
            "As the goal is to place cards from left to right, from 2 to King, the goal of each round should be to extend the number of cards in the correct place."+
            "  I.e., the goal of the first round(s) is to get the 2s into place first, and then add cards appropriately to the right of the 2s.\n"+
            "A round ends when all spaces are to the right of Kings.  When a round ends, the player clicks the \"Next Round\" button."+
            "  At this point, all cards that are not in the correct places on the board (from left to right) are removed, shuffled, and replaced."+
            "  Thus, the cards that have been correctly placed from left to right are saved.  The goal is to finish the game, ending up with all cards in place.\n"+
            "Points are awarded as follows: each card that is placed correctly in round 1 yields 10 points, each card placed correctly in round 2 yields 9 points, and so on."+
            "  The highest score possible is 480 points -- getting all 48 cards in place with the spaces in the farthest right column, in the first round."+
            "  The highest score recorded is stored permanently.",
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
          date: "Before Fall 2016"
        },
        {
          id: "snake_game.py",
          name: "New Snake",
          details: "A better version of the classic Snake game than the one below.",
          image: $scope.picturePath + "snake2.png",
          instructions: "Use the arrow keys to control your snake's movement.  Collect the red things to get longer.  Going off the edge on one side results in showing up on the other.",
          author: "Tristan Hazlett",
          date: "Fall 2016" 
        },
        {
          id: "driver.py",
          name: "Snake",
          details: "A clone of the classic Snake game.",
          image: $scope.picturePath + "snake.png",
          instructions: "Use the arrow keys to control your snake's movement.  Collect the red things to get longer.  Going off the edge on one side results in showing up on the other.",
          author: "Unknown",
          date: "Before Fall 2016"
        },
        {
          id: "driver.py",
          name: "Othello (Kinda)",
          details: "Othello game (mostly broken).",
          image: $scope.picturePath + "othello.png",
          instructions: "This game doesn't actually work, so don't play it.",
          author: "Unknown",
          date: "Before Fall 2016"
        },
        {
          id: "driver.py",
          name: "Super Tic Tac Toe",
          details: "Not your grandma's tic tac toe -IGN",
          image: $scope.picturePath + "super_tictactoe.png",
          instructions: "Instructions coming soon.",
          author: "Unknown",
          date: "Before Fall 2016"
        }
    ],
    'independent': [
        {
          id: "GuiApp1",
          name: "Java Gui",
          details: "Java test...",
          instructions: "Really nothing to do here.  Just look and enjoy! :)",
          author: "Joel Stehouwer",
          date: "Fall 2016"
        },
        {
          id: "HelloWorld",
          name: "Java Console",
          details: "Java test, check logs/java_try.log...",
          instructions: "Really nothing to do here.  Just look and enjoy! :)",
          author: "Joel Stehouwer",
          date: "Fall 2016"
        },
        {
          id: "RPSS.jar",
          name: "RPSS",
          details: "Greenfoot thing",
          author: "Victor Norman",
          date: "03/07/2017"
        }
    ],
    'cs112': [
        {
          id: "main",
          name: "C++ Console",
          details: "C++ program",
          instructions: "Really nothing to do here.  Just look and enjoy! :)",
          author: "Joel Stehouwer",
          date: "Fall 2016"
        }
    ],
    'cs212': [
        {
          id: "hello.exe",
          name: "C# Console",
          details: "C# program",
          instructions: "Really nothing to do here.  Just look and enjoy! :)",
          author: "Andrew Lang",
          date: "Fall 2016"
        },
        {
          id: "CSharpGui.exe",
          name: "C# Gui",
          details: "C# Gui Program",
          instructions: "Really nothing to do here.  Just look and enjoy! :)",
          author: "Andrew Lang",
          date: "Fall 2016"
        },
    ]
  };
}]);
