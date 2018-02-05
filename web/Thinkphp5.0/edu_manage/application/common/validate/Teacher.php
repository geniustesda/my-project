<?php
/**
 * Created by PhpStorm.
 * User: Admin 2017-2-8
 * Date: 2018-02-02
 * Time: 15:20
 */
namespace app\common\validate;
use think\Validate;

class Teacher extends Validate
{
    protected $rule = [
        'email' => 'email',
    ];
}