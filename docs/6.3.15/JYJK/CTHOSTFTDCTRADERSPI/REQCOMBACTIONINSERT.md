<p>申请组合录入请求</p>
<p>错误响应: OnErrRtnCombActionInsert，OnRspCombActionInsert</p>
<p>正确响应: OnRtnCombAction</p>
<span class="anchor" id="f12ae962-7566-4bd7-81a1-e078c633aee2"></span>
## 1.函数原型
<p>virtual int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) = 0;</p>
<span class="anchor" id="0285cd1a-61a0-447c-adf1-43b36f631418"></span>
## 2.参数
<p>pInputCombAction：输入的申请组合</p>
<pre><code>struct CThostFtdcInputCombActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///组合引用
    TThostFtdcOrderRefType CombActionRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///数量
    TThostFtdcVolumeType Volume;
    ///组合指令方向
    TThostFtdcCombDirectionType CombDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3d184c26-40b0-4866-a5ad-4bebd28737ab"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="290bd805-114a-4fb6-be34-e1f58728d5cf"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e2ac6489-7ff2-40fa-91ba-4fbc018671f0"></span>
## 5.FAQ
<p>无</p>
