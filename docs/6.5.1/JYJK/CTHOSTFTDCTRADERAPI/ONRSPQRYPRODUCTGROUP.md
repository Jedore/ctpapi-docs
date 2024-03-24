<p>请求查询产品组，当执行ReqQryProductGroup后，该方法被调用。</p>
<span class="anchor" id="cfef3c76-d079-4686-9047-3c93f9b50393"></span>
## 1.函数原型
<p>virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7cfafc4b-1fb8-46b3-b774-0a004ae3d917"></span>
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
<span class="anchor" id="c0f52df0-3ebb-4bc1-8f5f-15f81fa156c1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8c47186b-2029-4700-9fae-d57e3dbb94ba"></span>
## 4.FAQ
<p>无</p>
