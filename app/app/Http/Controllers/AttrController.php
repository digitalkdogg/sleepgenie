<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Attribute;

class AttrController extends Controller
{
    public function index() 
    {
        $attrs = Attribute::all();
        return response()->json($attrs);
    }

    public function byName($name) {
      $attrss = Attribute::where('Name', $name)->get();
      return response()->json($attrss);
    }
}
