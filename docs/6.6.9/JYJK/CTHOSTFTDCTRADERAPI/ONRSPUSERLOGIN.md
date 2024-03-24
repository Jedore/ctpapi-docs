<p>登录请求响应，当执行<a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGIN/">ReqUserLogin</a>后，该方法被调用。</p>
<span class="anchor" id="3d55b883-884f-41d0-a47c-39e54244b260"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5559f57a-fbf8-406d-a009-9c72ffc9fee4"></span>
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
    TThostFtdcSysVersionType SysVersion;
    ///广期所时间
    TThostFtdcTimeType GFEXTime;
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
<span class="anchor" id="eaf56107-8a49-496e-9a50-21a6ac99146b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="39f1a9bd-dd40-44fd-b259-873830384a43"></span>
## 4.FAQ
<p>无</p>
