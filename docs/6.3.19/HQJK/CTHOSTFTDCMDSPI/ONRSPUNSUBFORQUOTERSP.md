<p>取消订阅询价应答，当UnSubscribeForQuoteRsp后，调用此接口。</p>
<span class="anchor" id="95c7d2bb-6cdc-46f5-98f1-f1e6357f84be"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="325f0068-845e-4907-9be7-8bd5da2c927c"></span>
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
<span class="anchor" id="abff5ccb-7716-4be3-9fd3-b5624aff0440"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ab5d51d4-3301-483b-896e-bf78e1f002ea"></span>
## 4.FAQ
<p>无</p>
