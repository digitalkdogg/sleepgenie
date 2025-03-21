<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AttrController;
use App\Http\Controllers\MetaController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});
Route::get('/Attrs', [AttrController::class, 'index']);
Route::get('/Attrs/{name}', [AttrController::class, 'byName']);
Route::get('/Attrs/file/2', [AttrController::class, 'byFile']);
Route::get('/Meta/', [MetaController::class, 'index']);
Route::get('/Meta/{service}', [MetaController::class, 'byService']);
Route::get('/Meta/name/{name}', [MetaController::class, 'byName']);
Route::get('/Meta/file/2', [MetaController::class, 'fromFile']);
