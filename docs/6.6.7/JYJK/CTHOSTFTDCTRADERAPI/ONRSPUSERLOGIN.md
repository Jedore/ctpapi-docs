<p>登录请求响应，当执行<a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGIN/">ReqUserLogin</a>后，该方法被调用。</p>
<span class="anchor" id="bd61aa01-da78-4dd9-94ee-f6b981cf2188"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a8b4c684-5670-4046-86b9-2f0594b2cd2c"></span>
## 2.参数
<p>pRspUserLogin：用户登录应答</p>
<pre><code>struct CThostFtdcRspUserLoginField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///登录成功时间
    TThostFtdcTimeType LoginTime;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///交易系统名称
    TThostFtdcSystemNameType SystemName;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///最大报单引用
    TThostFtdcOrderRefType MaxOrderRef;
    ///上期所时间
    TThostFtdcTimeType SHFETime;
    ///大商所时间
    TThostFtdcTimeType DCETime;
    ///郑商所时间
    TThostFtdcTimeType CZCETime;
    ///中金所时间
    TThostFtdcTimeType FFEXTime;
    ///能源中心时间
    TThostFtdcTimeType INETime;
    ///后台版本信息
    TThostFtdcSysVersionType    SysVersion;
};
</code></pre>
<p>SysVersion：柜台版本号</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="ee95af85-bc26-4e95-8abf-57fc1a4e3922"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ecf60fa1-dc45-41f6-9405-18c9310d1f30"></span>
## 4.FAQ
<p>无</p>
