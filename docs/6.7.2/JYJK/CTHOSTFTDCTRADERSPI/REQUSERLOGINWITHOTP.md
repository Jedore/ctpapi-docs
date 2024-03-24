<p>用户发出带有动态口令的登陆请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERLOGIN/">OnRspUserLogin</a></p>
<span class="anchor" id="e055ec0e-3991-4342-878b-0c434fe51ac8"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithOTP(CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID) = 0;</p>
<span class="anchor" id="24420274-b34c-4129-9c7f-fb2e167c9496"></span>
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
<span class="anchor" id="5700edf5-0c4e-47e3-865d-3714d4e08e53"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="31c12209-2ab5-46e2-b353-9b8185e37abb"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="10c06361-4dd4-44d2-9e2e-04a01f7dfaa8"></span>
## 5.FAQ
<p>无</p>
