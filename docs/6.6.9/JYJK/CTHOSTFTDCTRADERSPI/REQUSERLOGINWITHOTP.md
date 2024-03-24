<p>用户发出带有动态口令的登陆请求，暂不支持</p>
<p>响应: <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a></p>
<span class="anchor" id="fe6b1655-ae62-4c46-8b95-e7c9bd057643"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithOTP(CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID) = 0;</p>
<span class="anchor" id="7c4ef471-db0d-4947-8be9-4a27c515e175"></span>
## 2.参数
<p>pReqUserLoginWithOTP：用户发出带动态验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithOTPField
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
    ///OTP密码
    TThostFtdcPasswordType  OTPPassword;
    ///终端IP端口
    TThostFtdcIPPortType    ClientIPPort;
    ///终端IP地址
    TThostFtdcIPAddressType ClientIPAddress;
};
</code></pre>
<p>ClientIPAddress：填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ecef2953-f19c-4a18-bef1-def205b13e6a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="49e42b7e-94cf-4fb2-b282-53b26aa84afa"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6f31ea78-1110-43cd-9176-e9e23f914127"></span>
## 5.FAQ
<p>无</p>
