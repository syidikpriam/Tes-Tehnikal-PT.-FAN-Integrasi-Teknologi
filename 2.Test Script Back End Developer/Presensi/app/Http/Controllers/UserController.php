<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\hash;

class UserController extends Controller
{
    public function __construct()
    {
        $this->middleware('auth');
    }

    function index()
    {
        $users = User::get();
        return view('user', [
            'users' =>$users
        ]);
    }

    function create()
    {
        return view('create-user');
    }

    function store(Request $request)
    {
        User::create([
            'name' => $request->name,
            'email' => $request->email,
            'npp' => $request->npp,
            'npp_supervisor' => $request->npp_supervisor,
            'password' => hash::make($request->password),
        ]);


        // return redirect()->route('user');
        return redirect()->action('App\Http\Controllers\UserController@index');
    }
}
