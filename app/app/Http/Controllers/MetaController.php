<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Meta;

class MetaController extends Controller
{
    public function index() 
    {
        $meta = Meta::all();
        return response()->json($meta);
    }

    public function byName($name) {

        $metas = Meta::where('Name', $name)->get();
        return response()->json($metas);
    }

    public function byService($service) {

        $metas = Meta::where('serviceID', $service)->get();
        return response()->json($metas);
    }
}
