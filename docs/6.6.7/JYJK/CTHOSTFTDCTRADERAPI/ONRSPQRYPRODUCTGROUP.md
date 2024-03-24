<p>请求查询产品组，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTGROUP/">ReqQryProductGroup</a>后，该方法被调用。</p>
<span class="anchor" id="07d99c56-d33c-42ac-9e83-d13c9286eacc"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7fbc950d-e224-4990-a6ce-348aca41b52f"></span>
## 2.参数
<p>pProductGroup：投资者品种/跨品种保证金产品组</p>
<pre><code>struct CThostFtdcProductGroupField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve2;
    ///产品代码
    TThostFtdcInstrumentIDType  ProductID;
    ///产品组代码
    TThostFtdcInstrumentIDType  ProductGroupID;
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
<span class="anchor" id="832e7f26-e086-40d6-8eca-ebc41354508a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e66b5258-a2a4-48d8-adf8-4ebcc41a9d4f"></span>
## 4.FAQ
<p>无</p>
