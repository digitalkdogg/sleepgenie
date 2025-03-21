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

    public function fromFile() {
      $json = [json_decode('{"id":1,"Name":"Score","serviceID":2},{"id":4,"Name":"Resting Heart Rate","serviceID":2},{"id":5,"Name":"Body Battery","serviceID":2},{"id":6,"Name":"Respiration","serviceID":2},{"id":7,"Name":"Quality","serviceID":2},{"id":8,"Name":"Duration","serviceID":2},{"id":9,"Name":"Bedtime","serviceID":2},{"id":16,"Name":"Wake Time","serviceID":2}')];
      return response()->json($json);
    }
}
