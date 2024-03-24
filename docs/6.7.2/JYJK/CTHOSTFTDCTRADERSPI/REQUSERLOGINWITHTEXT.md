<p>用户发出带有短信验证码的登陆请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERLOGIN/">OnRspUserLogin</a></p>
<span class="anchor" id="2582fda2-ef47-4767-a277-61b490f41fea"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithText(CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID) = 0;</p>
<span class="anchor" id="467591bf-00b4-4f48-b05f-f3344c842eeb"></span>
## 2.参数
<p>pReqUserLoginWithText：用户发出带短信验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithTextField
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
    ///短信验证码文字内容
    TThostFtdcPasswordType  Text;
    ///终端IP端口
    TThostFtdcIPPortType    ClientIPPort;
    ///终端IP地址
    TThostFtdcIPAddressType ClientIPAddress;
};
</code></pre>
<p>ClientIPAddress：填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="391acb8d-ed51-4b5c-a1f7-dc2531fe0ee1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1a4a4cbd-4b40-4832-9f76-78d5e408e061"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="dba330f4-5206-45b0-a645-11179c0b0447"></span>
## 5.FAQ
<p>无</p>
