<p>订阅询价应答，当调用SubscribeForQuoteRsp后，通过此接口返回。</p>
<span class="anchor" id="c991f29c-d636-45b9-a39e-9e39307a48dc"></span>
## 1.函数原型
<p>virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6914b980-0aaa-469e-a57a-6461f3e0ed8a"></span>
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
<span class="anchor" id="1b370fd9-65b8-484b-a47c-114e9b1db7e9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f02b6102-92dc-4a26-ba74-a14172b20fa5"></span>
## 4.FAQ
<p>无</p>
