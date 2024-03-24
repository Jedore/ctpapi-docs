<p>取消订阅询价应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEFORQUOTERSP/">UnSubscribeForQuoteRsp</a>后，调用此接口。</p>
<span class="anchor" id="887dc623-f9b0-407f-baca-6ab49c78a355"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="79babcb6-77e8-47ab-ac59-7db4c56343a0"></span>
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
<span class="anchor" id="4badc0a7-aa6a-4383-9d27-1703486fbbfb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="22d648e4-fdb6-4b23-a0ae-67badd6e599a"></span>
## 4.FAQ
<p>无</p>
