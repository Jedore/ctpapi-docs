<p>请求查询产品组，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTGROUP/">ReqQryProductGroup</a>后，该方法被调用。</p>
<span class="anchor" id="28abef3e-ebb8-43ac-a7f6-3f24eed93d5b"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c5b10ac9-307d-4765-b328-e7fa3fc58723"></span>
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
<span class="anchor" id="75707b1f-9799-428b-be0d-82093bb947c7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="be0ea877-041e-445d-9d0a-684896779f5c"></span>
## 4.FAQ
<p>无</p>
