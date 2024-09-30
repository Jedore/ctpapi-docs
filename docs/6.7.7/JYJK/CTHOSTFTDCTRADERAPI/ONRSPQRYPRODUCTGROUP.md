<p>请求查询产品组，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTGROUP/">ReqQryProductGroup</a>后，该方法被调用。</p>
<span class="anchor" id="7a347b13-0877-465a-8338-f5f844f705d6"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d482463a-7bf6-479d-9b58-d8b5af2fbd61"></span>
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
<span class="anchor" id="9832203e-d20a-4ae0-b463-91a4564fd1d0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8ea23067-a926-4ff0-a547-f21c7e9d4367"></span>
## 4.FAQ
<p>无</p>
