<p>用户发出带有图片验证码的登陆请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERLOGIN/">OnRspUserLogin</a></p>
<span class="anchor" id="4ca38923-f105-4c99-9eb2-efe2c9044974"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithCaptcha(CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="4512acc8-8186-4224-b04d-72ccd9ba9160"></span>
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
<span class="anchor" id="45f842d7-b62e-4496-b965-4c93ce858af8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7d2f300f-43ff-47f8-b99f-c2eaf7cd82e1"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0a8d0e93-9071-4314-b33c-6c86145714c5"></span>
## 5.FAQ
<p>无</p>
