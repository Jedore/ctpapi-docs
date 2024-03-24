<p>用户发出带有图片验证码的登陆请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERLOGIN/">OnRspUserLogin</a></p>
<span class="anchor" id="226e376d-8d4f-4482-a941-d4207beb5795"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithCaptcha(CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="fe2a6abb-327e-4d25-9d4c-07ece4905054"></span>
## 2.参数
<p>pReqUserLoginWithCaptcha：用户发出带图形验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithCaptchaField
{
///交易日
TThostFtdcDateType  TradingDay;
///经纪公司代码
TThostFtdcBrokerIDType  BrokerID;
///用户代码
TThostFtdcUserIDType    UserID;
///密码
TThostFtdcPasswordType  Password;
///用户端产品信息
TThostFtdcProductInfoType   UserProductInfo;
///接口端产品信息
TThostFtdcProductInfoType   InterfaceProductInfo;
///协议信息
TThostFtdcProtocolInfoType  ProtocolInfo;
///Mac地址
TThostFtdcMacAddressType    MacAddress;
///保留的无效字段
TThostFtdcOldIPAddressType  reserve1;
///登录备注
TThostFtdcLoginRemarkType   LoginRemark;
///图形验证码的文字内容
TThostFtdcPasswordType  Captcha;
///终端IP端口
TThostFtdcIPPortType    ClientIPPort;
///终端IP地址
TThostFtdcIPAddressType ClientIPAddress;
};
</code></pre>
<p>ClientIPAddress：填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="41cf404c-1da8-4c67-ac4d-f426f688869d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="61b3029d-43ab-4357-ab6d-59c7283dd6cc"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="16110319-50b8-4065-9bc3-7b1b43e70cd1"></span>
## 5.FAQ
<p>无</p>
