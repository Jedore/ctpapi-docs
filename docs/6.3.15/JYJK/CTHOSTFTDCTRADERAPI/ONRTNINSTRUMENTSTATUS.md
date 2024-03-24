<p>合约交易状态通知，主动推送。私有流回报。</p>
<span class="anchor" id="4bc311f3-b488-4126-a7fa-a137c7ef6d94"></span>
## 1.函数原型
<p>virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {};</p>
<span class="anchor" id="1d0ef2b5-c27d-4658-b296-44da7ed29a36"></span>
## 2.参数
<p>pInstrumentStatus：合约状态</p>
<pre><code>struct CThostFtdcInstrumentStatusField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///结算组代码
    TThostFtdcSettlementGroupIDType SettlementGroupID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///合约交易状态
    TThostFtdcInstrumentStatusType InstrumentStatus;
    ///交易阶段编号
    TThostFtdcTradingSegmentSNType TradingSegmentSN;
    ///进入本状态时间
    TThostFtdcTimeType EnterTime;
    ///进入本状态原因
    TThostFtdcInstStatusEnterReasonType EnterReason;
};
</code></pre>
<span class="anchor" id="1b337665-8466-43b5-8b51-31cb43232027"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="43e83047-5e60-47ec-b0ed-2b3b32ee1aaf"></span>
## 4.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如何获取期权合约的状态？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>期权合约状态暂时不推送。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
