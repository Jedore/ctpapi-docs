<p>申请组合录入请求</p>
<p>错误响应: OnErrRtnCombActionInsert，OnRspCombActionInsert</p>
<p>正确响应: OnRtnCombAction</p>
<span class="anchor" id="652e9800-d47a-4951-891b-49156840c600"></span>
## 1.函数原型
<p>virtual int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) = 0;</p>
<span class="anchor" id="bac09112-91d8-4644-9186-73306bd7cdd0"></span>
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
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ab5839bc-8983-4b48-8339-faff44a01843"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="db1f94d3-191c-40e3-9bfa-b2da8e786acf"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="3a029741-06cd-4fec-9abc-a44e0d47578f"></span>
## 5.FAQ
<p>无</p>
