<p>登录请求响应，当ReqUserLogin后，该方法被调用。</p>
<span class="anchor" id="80a74c67-ab2b-4bce-8296-dda2f3d81869"></span>
## 1.函数原型
<p>virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b40f7cf6-20a5-40f0-9350-0932671e36cc"></span>
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
};
</code></pre>
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
<span class="anchor" id="58ad6b64-071c-4503-af8c-3d7cc8bf03ab"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7d621940-6f5c-4bd3-a5b8-2a95c5fe65d5"></span>
## 4.FAQ
<p>无</p>
