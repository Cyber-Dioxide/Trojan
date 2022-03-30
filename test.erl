%%%-------------------------------------------------------------------
%%% @author Saad Khan
%%% @copyright (C) 2022, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 12. Mar 2022 6:11 PM
%%%-------------------------------------------------------------------
-module(test).
-author("Saad Khan").

%% API
-export([start/0]).

start() ->
  X = 10,
  Y = 20,
  Reult = X+Y,
  io:fwrite("~n" , [Reult]).
