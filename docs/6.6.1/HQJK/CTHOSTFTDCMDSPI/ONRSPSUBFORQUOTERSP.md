<p>订阅询价应答，当调用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>后，通过此接口返回。</p>
<span class="anchor" id="175de230-2078-4ffc-b20b-c725d9483789"></span>
## 1.函数原型
<p>virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5a3655f1-4159-4a24-a1b1-075cd5ad490b"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="6cee1ccf-8e4d-43f2-a44b-4347972bcbfa"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2cae88d8-e088-475e-878c-8e9f6ac55519"></span>
## 4.FAQ
<p>无</p>
