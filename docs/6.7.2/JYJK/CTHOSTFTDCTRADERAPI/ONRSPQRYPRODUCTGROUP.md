<p>请求查询产品组，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTGROUP/">ReqQryProductGroup</a>后，该方法被调用。</p>
<span class="anchor" id="32528618-92d2-485a-b81e-cf29ca5258f7"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="631c4706-68ed-4d07-a871-1752119e8e17"></span>
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
<span class="anchor" id="34e13fd7-a832-45fe-b08b-ffaf61b190da"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ae36f2cc-0d5d-4595-9774-ac813768890e"></span>
## 4.FAQ
<p>无</p>
