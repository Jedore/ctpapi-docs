<p>请求查询产品组，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTGROUP/">ReqQryProductGroup</a>后，该方法被调用。</p>
<span class="anchor" id="ecb96717-2639-4416-af5d-ac01c807215f"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8bc177f1-fc62-48f8-871e-646c4ea48ed6"></span>
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
<span class="anchor" id="dfa6338b-9030-4330-bc27-19273b9c9034"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a8c66c24-d656-46b5-9714-4b57e9b48303"></span>
## 4.FAQ
<p>无</p>
