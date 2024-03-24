<p>请求查询产品组，当执行ReqQryProductGroup后，该方法被调用。</p>
<span class="anchor" id="2a66c8a3-4eed-4c3d-bf46-6eca328e86e2"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8df78569-0050-4d34-8ff5-3202e63d5cfd"></span>
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
<span class="anchor" id="9772ccfc-2627-4980-9cac-5a2e35974c52"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="003fa268-e1fe-46b4-adb3-40420caefd6c"></span>
## 4.FAQ
<p>无</p>
