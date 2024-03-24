<p>请求查询产品组，当执行ReqQryProductGroup后，该方法被调用。</p>
<span class="anchor" id="fd1bf1e0-0788-43cb-b84c-62759ca9d5eb"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="50916a3b-e349-4b12-a2e6-e1271e8c811a"></span>
## 2.参数
<p>pProductGroup：投资者品种/跨品种保证金产品组</p>
<pre><code>struct CThostFtdcProductGroupField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///产品组代码
    TThostFtdcInstrumentIDType ProductGroupID;
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
<span class="anchor" id="10fa1602-2856-4351-a16f-8c46dfc7e082"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3a8ba321-e29c-4b9b-8bbe-6fae2f2b8646"></span>
## 4.FAQ
<p>无</p>
